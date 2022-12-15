export function redraw(xl, yt, xr, yb, cx, cy) {

    // clear canvas
    ctx.clearRect(0, 0, viewbox.width, viewbox.height);
    
    // set drawing params
    ctx.fillStyle = "rgb(3, 160, 256, 0.05)";
    ctx.strokeStyle = "rgb(3, 160, 256, 0.8)";
    ctx.lineWidth = 0.8;
    ctx.setLineDash([0, 0]);

    // draw and fill viewbox
    ctx.fillRect(xl, yt, xr-xl, yb-yt);
    ctx.strokeRect(xl, yt, xr - xl, yb - yt);
    
    // draw in crosshairs
    ctx.beginPath();
    ctx.moveTo(xl, (yb + yt) / 2);
    ctx.lineTo(xr, (yb + yt) / 2);
    ctx.stroke(); 

    ctx.moveTo((xr + xl) / 2, yt);
    ctx.lineTo((xr + xl) / 2, yb);
    ctx.stroke(); 

    // draw sub-crosshairs
    ctx.strokeStyle = "rgb(3, 160, 256, 0.8)";
    ctx.lineWidth = 0.4;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(xl + (xr - xl) / 4, yt);
    ctx.lineTo(xl + (xr - xl) / 4, yb);
    ctx.moveTo(xl + (xr - xl) * (3 / 4), yt);
    ctx.lineTo(xl + (xr - xl) * (3 / 4), yb);
    ctx.moveTo(xl, yt + (yb - yt) / 4);
    ctx.lineTo(xr, yt + (yb - yt) / 4);
    ctx.moveTo(xl, yt + (yb - yt) * (3 / 4));
    ctx.lineTo(xr, yt + (yb - yt) * (3 / 4));
    ctx.stroke();

    // draw in cursor
    ctx.fillStyle = "rgb(255, 255, 255, 1.0)";
    ctx.strokeStyle = "rgb(0, 0, 0, 1.0)";
    ctx.lineWidth = 1.0;
    ctx.setLineDash([0, 0]);
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(cx + 12, cy + 12);
    ctx.lineTo(cx + 6, cy + 12);
    ctx.lineTo(cx + 8, cy + 16);
    ctx.lineTo(cx + 6, cy + 17);
    ctx.lineTo(cx + 4, cy + 13);
    ctx.lineTo(cx, cy + 16.97);
    ctx.lineTo(cx, cy);
    ctx.stroke();
    ctx.fill();

    console.log('redraw() called!');
};