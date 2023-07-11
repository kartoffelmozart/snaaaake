console.log("Mads er tyk")

const canvas = document.getElementsByTagName("canvas")[0];
  //  const canvas = document.querySelector("#canvas");
const ctx = canvas.getContext("2d");
const canvasHeight = canvas.clientHeight;
const canvasWidth = canvas.clientWidth;
const cellSize = 50;

function drawGrid() {

    ctx.strokeStyle = "grey"
    ctx.lineWidth = 0.3

    for (let currentColumn = cellSize; currentColumn < canvasWidth; currentColumn+=cellSize) {
        ctx.moveTo(currentColumn,0)
        ctx.lineTo(currentColumn,canvasHeight)
        ctx.stroke();
    }

    for (let currentRow = cellSize; currentRow < canvasHeight; currentRow+=cellSize) {
        ctx.moveTo(0,currentRow)
        ctx.lineTo(canvasWidth,currentRow)
        ctx.stroke()
    }
}

drawGrid()