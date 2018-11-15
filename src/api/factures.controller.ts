import { Request, Response } from 'express';
import { Client } from 'cassandra-driver';
import { Facture } from '../models/facture.model';

export class FactureController {
    public async addFacture(req: Request, res: Response) {
        const cassandraUri = process.env.CASSANDRA_URI;
        const facture = req.body as Facture;

        const client = new Client({ contactPoints: [cassandraUri] });
        await client.connect();

        // TODO: Enregistrer dans la BD
        const query = `INSERT INTO factures.factures JSON '${JSON.stringify(facture)}'`;
        await client.execute(query);
        res.sendStatus(200);
    }

    public getProduitsFrequents(req: Request, res: Response) {
        // TODO: Poker le serveur

        res.send({ message: 'Not implemented' });
    }
}
/*
CREATE TABLE factures.factures (
	id uuid,
	products MAP<text, varint>,
	PRIMARY KEY (id)
);
*/