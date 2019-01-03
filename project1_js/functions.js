let {PythonShell} = require('python-shell');
let fs = require('fs');
let logger = require('electron-log/renderer');


function makeLog(name) {
    logger.info(name);
}
// require('./main.js');

/*
function deleteFile() {
    alert('delete');
}
*/

var buttonRunText = document.getElementById('newWindowButton');
buttonRunText.addEventListener('click', function () {
    window.open('first_window_test.html','', 'width=1200');
});

// var buttonRunScript = document.getElementById('myButton');
// buttonRunScript.addEventListener('click', function () {
//     document.getElementById('KisLabel').innerHTML = 'super Kis';
//     makeLog('SuperKis');
// });


// var buttonOnePlusOne = document.getElementById('pythonButton');
// buttonOnePlusOne.addEventListener('click', function () {
//     PythonShell.runString('import sys; x=1+1; print(x); sys.stdout.flush()', null, function (err, results) {
//             if (err) makeLog('ERROR ' + err);
//             makeLog(results);
//             document.getElementById('sum').innerHTML = '= ' + results;
//         }
//     )
// });


// var buttonRunProg = document.getElementById('go!');
// buttonRunProg.addEventListener('click', function () {
//     PythonShell.run('test_time_interpreter.py', null, function (err, results) {
//         if (err) makeLog('ERROR ' + err);
//         makeLog(results);
//         document.getElementById('time').innerHTML = results;
//     })
// });


var fromTextArea;
let options = {
    mode: 'text',
    args: []
};

var translatorFileInput = document.getElementById('translatorsFiles');
// translatorFileInput.addEventListener('change', function () {
//     for (let i = 0; i < translatorFileInput.files.length; i++) {
//         options.args.push(translatorFileInput.files[i].name);
//         options.args.push(translatorFileInput.files[i].path);
//         makeLog('added ' + translatorFileInput.files[i].name)
//     }
//
// });

var buttonFileCycle = document.getElementById('cycleArgs');
var textArea = document.getElementById('googleText');
buttonFileCycle.addEventListener('click', function () {
    var text_opt = fs.readFileSync('tempFiles\\options.args.txt', 'utf8');
    makeLog('text_opt: ' + text_opt);
    var textByLine = text_opt.split(",");
    for (strr of textByLine){
        options.args.push(strr);
    }
    fromTextArea = document.getElementById('googleText').value;
    options.args.push(fromTextArea);
    PythonShell.run('get_the_job_done2.py', options, function (err, results) {
        makeLog('options: ' + options.args);

        if (err) makeLog('ERROR ' + err);

        fs.writeFileSync('tempFiles\\test.html', '');
        var text = fs.readFileSync('tempFiles\\newfile.txt', 'utf8');
        fs.writeFileSync('test.html', text);

        window.open('test.html');
        for (let res of results) {
             makeLog(res);
        }


    })
});
