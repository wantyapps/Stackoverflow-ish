const express = require("express");
const app = express();
const path = require("path")

app.use(express.static(__dirname + "/public"))

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname + "/public/main.html"));
});

app.get("/api", (req, res) => {
	if ( req.headers.username == "wantyapps" && req.headers.password == "pass123" ) {
		res.send('{"username": "wantyapps", "password": "oao"}');
	} else {
		res.send("Incorrect username or password.");
	};
});

app.get("/about", (req, res) => {
	res.sendFile(path.join(__dirname + "/public/about.html"));
});

const PORT = 5000;

app.listen(PORT, () => console.log(`Server is listening on port ${PORT}`));
