import path from "path";
import { Readable } from "stream";
import { createHash } from "crypto";
import { spawn } from "child_process";
import { createReadStream, existsSync, mkdirSync } from "fs";

const rawFilesDir = path.join(__dirname, "r");

if (!existsSync(rawFilesDir)) {
    mkdirSync(rawFilesDir);
}

const getArgs = (input: string, output: string) =>
    (
        "-y " +
        `-i ${input} ` +
        "-c copy " +
        "-acodec pcm_s16le " +
        "-f s16le " +
        "-ac 1 " +
        "-ar 68000 " +
        output
    ).split(/\s/);

const getOutput = (input: string) =>
    path.join(rawFilesDir, createHash("md5").update(input).digest("hex"));

export default (input: string): Promise<Readable> => {
    return new Promise((resolve, reject) => {
        const output = getOutput(input);

        if (existsSync(output)) {
            resolve(createReadStream(output));
            return;
        }

        const process = spawn("ffmpeg", getArgs(input, output));

        process.on("exit", (code) => {
            if (code != 0) {
                reject(new Error(`Got a non-zero return code: ${code}`));
                return;
            }

            resolve(createReadStream(output));
        });
    });
};
