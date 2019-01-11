let {PythonShell} = require('python-shell');
let fs = require('fs');
let logger = require('electron-log/renderer');
var globalFileIdNumber = 0;
var arrayFiles = [];
const { dialog } = require('electron').remote;




function makeLog(name) {
    logger.info(name);
}


// var buttonRunText = document.getElementById('newWindowButton');
// buttonRunText.addEventListener('click', function () {
//     window.open('second_window_test.html', '', 'width=800, height=500');
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
    // makeLog('text_opt: ' + text_opt);
    var textByLine = text_opt.split(",");
    for (strr of textByLine) {
        options.args.push(strr);
    }
    fromTextArea = document.getElementById('googleText').value;
    options.args.push(fromTextArea);
    PythonShell.run('get_the_job_done2.py', options, function (err, results) {
        makeLog('options: ' + options.args);

        if (err) {makeLog('ERROR ' + err);
        alert(err)}

        fs.writeFileSync('tempFiles\\test.html', '');
        var text = fs.readFileSync('tempFiles\\newfile.txt', 'utf8');
        fs.writeFileSync('test.html', text);

        window.open('test.html', '', 'width=1200,height=600');
        document.getElementById('reset').style.display = 'inline'
        for (let res of results) {
            makeLog(res);
        }


    })
});

buttonFileCycle.addEventListener('click', function () {
    document.getElementById('mur').style.display = 'none';
    document.getElementById('label').style.display = 'none';
    document.getElementById('cycleArgs').style.display = 'none';
    document.getElementById('nameList').style.display = 'none';
    document.getElementById('googleText').style.display = 'none';
    document.body.style.cursor = "wait !important";

});
var buttonReset = document.getElementById('reset');
buttonReset.addEventListener('click', function () {
    document.getElementById('mur').style.display = 'inline';
    document.getElementById('label').style.display = 'block';
    document.getElementById('cycleArgs').style.display = 'inline';
    document.getElementById("nameList").innerHTML = '';
    document.getElementById('nameList').style.display = 'inline';
    document.getElementById('googleText').value = '';
    document.getElementById('googleText').style.display = 'inline';
    document.getElementById('reset').style.display = 'none';
    options.args.length = 0
});