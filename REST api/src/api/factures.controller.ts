import { Request, Response } from 'express';
import { Client } from 'cassandra-driver';
import { Facture } from '../models/facture.model';

export class FactureController {
    public async addFacture(req: Request, res: Response) {
        const facture = req.body as Facture;

        // Connect to DB
        const cassandraUri = process.env.CASSANDRA_URI;
        const client = new Client({ contactPoints: [cassandraUri] });
        await client.connect();

        // Insertin DB
        const query = `INSERT INTO factures.factures JSON '${JSON.stringify(facture)}'`;

        try {
            await client.execute(query);
        }
        catch (err) {
            return res.status(500).send({ message: 'Unable to add.' });
        }

        res.sendStatus(200);
    }

    public getProduitsFrequents(req: Request, res: Response) {
        // TODO: Poker le serveur

        res.sendStatus(501);
    }
}
