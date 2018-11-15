import { Request, Response } from 'express';
import { Client, ClientOptions } from 'cassandra-driver';
import { Facture } from '../models/facture.model';

export class FactureController {
    public addFacture(req: Request, res: Response) {
        const facture = req.body as Facture;

        // TODO: Enregistrer dans la BD

        res.send({ message: 'Not implemented' });
    }

    public getProduitsFrequents(req: Request, res: Response) {
        // TODO: Poker le serveur

        res.send({ message: 'Not implemented' });
    }
}