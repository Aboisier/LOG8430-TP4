import { Request, Response } from 'express';
import { Client } from 'cassandra-driver';
import { Receipt } from '../models/receipt.model';

export class ReceiptsController {
    public async add(req: Request, res: Response) {
        const receipt = req.body as Receipt;

        // Connect to DB
        const cassandraUri = process.env.CASSANDRA_URI;
        const client = new Client({ contactPoints: [cassandraUri] });
        await client.connect();

        // Insert in DB
        const query = `INSERT INTO receipts.receipts JSON '${JSON.stringify(receipt)}'`;

        try {
            await client.execute(query);
            return res.sendStatus(200);
        }
        catch (err) {
            console.error(err);
        }

        return res.status(500).send({ message: 'Unable to add.' });
    }

    public async getAll(req: Request, res: Response) {
        // Connect to DB
        const cassandraUri = process.env.CASSANDRA_URI;
        const client = new Client({ contactPoints: [cassandraUri] });
        await client.connect();

        const query = `SELECT JSON id, products FROM receipts.receipts`;

        try {
            const result = await client.execute(query);
            const receipts = result.rows.map(x => JSON.parse(x['[json]'])) as Receipt[];
            return res.send(receipts);
        }
        catch (err) {
            console.error(err);
        }

        return res.status(500).send({ message: 'Unable to get all.' });
    }

    public getProduitsFrequents(req: Request, res: Response) {
        // TODO: Poker le serveur
        return res.sendStatus(501);
    }
}
