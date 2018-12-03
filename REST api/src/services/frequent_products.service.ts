const { exec } = require('child_process');

export class FrequentProductsService {
    public getFrequentProducts(): Promise<string> {
        const masterUri = process.env.MASTER_URI;
        return new Promise((resolve, reject) => {
            const command = `spark-submit --master ${masterUri} --packages anguenot:pyspark-cassandra:0.9.0 --conf spark.cassandra.connection.host=localhost ..\\Freq.py`;
            exec(command, (error: string, stdout: string, stderr: string) => {
                if (error) {
                    reject(error);
                    return;
                }
                resolve(stdout.trim());
            });
        });
    }
}