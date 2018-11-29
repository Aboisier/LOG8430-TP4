import express from 'express';
import bodyParser from 'body-parser';
import dotenv from 'dotenv';

import { ReceiptsController } from './api/receipt.controller';

// Load environment variables from .env file, where API keys and passwords are configured
dotenv.config();

// Controllers (route handlers)
const facturesController = new ReceiptsController();

// Create Express server
const app = express();

// Connect to CassandraDb

// Express configuration
app.set('port', process.env.PORT || 3000);
app.use(bodyParser.json());

// Primary app routes.
app.post('/', facturesController.add);
app.get('/', facturesController.getAll);
app.get('/frequent', facturesController.getProduitsFrequents);

export default app;