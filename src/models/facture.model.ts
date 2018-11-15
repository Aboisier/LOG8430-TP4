import { Produit } from "./produit.model";

export class Facture {
    constructor(public produits: Produit[]) { }
}