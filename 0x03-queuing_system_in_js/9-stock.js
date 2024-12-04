import { createClient } from 'redis';
import { promisify } from 'util';
import { express } from 'express'

// Defining the list of products
const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get item by ID
function getItemById(id) {
    return listProducts.find((product) => product.itemId === id);
}

// Creating the Redis client and ensuring the client returns a promise
// to be compatible with asynchronous ops
const redisClient = createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

redisClient.on('error', (err) => {
  console.error('Redis client error:', err.message);
});

// Handling stock management
async function reserveStockById(itemId, stock) {
    await setAsync(`item.${itemId}`, stock);
}
  
  async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock ? parseInt(stock, 10) : null;
}

// setting up an express server and defining the routes
const app = express();
const PORT = 1245;

// Route: Get all products
app.get('/list_products', async (req, res) => {
  res.json(listProducts);
});

// Route: Get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    currentStock !== null ? product.initialAvailableQuantity - currentStock : product.initialAvailableQuantity;

  res.json({ ...product, currentQuantity });
});

// Route: Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const reservedStock = currentStock !== null ? currentStock : 0;

  if (reservedStock >= product.initialAvailableQuantity) {
    return res.status(400).json({
      status: 'Not enough stock available',
      itemId,
    });
  }

  await reserveStockById(itemId, reservedStock + 1);

  res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});