import { createServer } from 'http'
import { callPython } from './communication.js'

async function handler(req, res) {
    const parsedUrl = new URL(req.url, `http://${req.headers.host}`)
    const interactions = parsedUrl.searchParams.get('interactions')

    let resultado = ''
    if(interactions){
        resultado = await callPython(interactions)
    }

    res.statusCode = 200
    res.setHeader('Content-Type', 'text/plain')
    res.end(resultado)
}

createServer(handler).listen(3333, () => {
    console.log('Running at 3333')
})