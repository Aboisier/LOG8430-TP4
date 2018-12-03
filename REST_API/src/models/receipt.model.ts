export class Receipt {
    constructor(public id: string, public products: { [name: string]: number }) { }
}