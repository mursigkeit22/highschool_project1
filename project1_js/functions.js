let {PythonShell} = require('python-shell');
let fs = require('fs');
let logger = require('electron-log/renderer');

function makeLog(name) {
    logger.info(name);
}

const buttonRunScript = document.getElementById('myButton');
buttonRunScript.addEventListener('click', function () {
    document.getElementById('KisLabel').innerHTML = 'super Kis';
    makeLog('SuperKis');
});


const buttonOnePlusOne = document.getElementById('pythonButton');
buttonOnePlusOne.addEventListener('click', function () {
    PythonShell.runString('import sys; x=1+1; print(x); sys.stdout.flush()', null, function (err, results) {
            if (err) makeLog('ERROR ' + err);
            makeLog(results);
            document.getElementById('sum').innerHTML = '= ' + results;
        }
    )
});


const buttonRunProg = document.getElementById('go!');
buttonRunProg.addEventListener('click', function () {
    PythonShell.run('test.py', null, function (err, results) {
        if (err) makeLog('ERROR ' + err);
        makeLog(results);
        document.getElementById('time').innerHTML = results;
    })
});


var fromTextArea;
let options = {
    mode: 'text',
    args: []
};

translatorFileInput = document.getElementById('translatorsFiles');
translatorFileInput.addEventListener('change', function () {
    for (let i = 0; i < translatorFileInput.files.length; i++) {
        options.args.push(translatorFileInput.files[i].name);
        options.args.push(translatorFileInput.files[i].path)
    }
});

const buttonFileCycle = document.getElementById('cycleArgs');
const textArea = document.getElementById('googleText');
buttonFileCycle.addEventListener('click', function () {
    fromTextArea = document.getElementById('googleText').value;
    options.args.push(fromTextArea);
    PythonShell.run('getting_files.py', options, function (err, results) {

        if (err) makeLog('ERROR ' + err);

        fs.writeFileSync('test.html', '');
        var text = fs.readFileSync('newfile.txt', 'utf8');
        fs.writeFileSync('test.html', text);

        window.open('test.html');
        for (let res of results) {
            makeLog(res);
        }

//
    })
});
