const minInput = document.querySelector("#alc-min");
const maxInput = document.querySelector("#alc-max");

minInput.addEventListener("click")

// I DONT FUCKING KNOWWWWWW HAHAHAHAH

async function runInceptionV2() {
    // Creat the session and load the pre-trained model
    const session = new onnx.InferenceSession({ backendHint: 'webgl' });
    await session.loadModel("../static/model.onnx")
    button.on("click",runInceptionV2);
    form.on("submit",runInceptionV2);
    var button = d3.select("#quality-button");
    var form = d3.select("#quality-form")

    const min = new d3.select("#alc-min").property("value");
    const max = new d3.select("#alc-max").propert("value");
  
    console.log(min);
    console.log(max);






}


// const myOnnxSession = new onnx.InferenceSession();
// myOnnxSession.loadModel("../static/model.onnx").then(()=>{
//     const inferenceInputs = getInputs();
//     session.run(inferenceInputs).then(output=>{
//     const outputTensor = output.values().value;
//     console.log(`model output tensor: ${outputTensor.data}.`);
//     });


// })
// model = onnx.load('../static/model.onnx')

// const sess = new oncontextmenu.InferenceSession()
// async function test(){
//     console.time("loading model")
//     await sess.loadModel("../static/model.onnx")
//     console.timeEnd("loading model")

//     console.log("model loaded");

// }

// document.querySelector('#load').addEventListener('click',test);



// sess = onnxruntime.InferenceSession('../static/model.onnx');
// {}