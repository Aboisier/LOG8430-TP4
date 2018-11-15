export class Facture {
    constructor(public id: string, public products: { [name: string]: number }) { }
}