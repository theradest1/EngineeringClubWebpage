const express = require('express');

const app = express();
const port = 3000;
const host = "0.0.0.0";

app.use(express.static("public"));
app.use("/css", express.static(__dirname + 'public/css'));
app.use("/js", express.static(__dirname + 'public/js'));
app.use("/img", express.static(__dirname + 'public/img'));

app.set('views', './views');

app.get("", (req, res) => {
	res.sendFile(__dirname + "/views/index.html");
});
app.get("/seaperch", (req, res) => {
	res.sendFile(__dirname + "/views/seaperch.html");
});

app.listen(port, host, () => {
	console.log("Server started on port " + port);
});
