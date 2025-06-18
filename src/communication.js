import { spawn } from 'child_process'
import { fileURLToPath } from 'url';
import path from 'path';

const filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(filename)

// File that contains the code in python
const pythonFile = path.join(__dirname, "bot.py")

// Command in python
const pythonCommand = "python"

// Function to call python
export async function callPython(interactions) {

    console.log(interactions)
    console.log(pythonFile)

    // 'Spawn' calls the command that runs python with a list of arguments to be passed
    const py = spawn(pythonCommand, [
        pythonFile,
        interactions
    ])

    py.stderr.on('data', (data) => {
        console.error(`LOG: ${data}`);
    });

    const dataString = []

    // 'stdout' outputs data asynchronously through a 'stream', using 'for await' waits for the data to return synchronously and adds the list of data
    for await(const log of py.stdout){
        dataString.push(log.toString())
    }

    // returns the concatenated data after execution
    return dataString.join('')
}