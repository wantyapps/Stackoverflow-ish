const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("NOT THE MAIN ROUTE");
});

app.get("/api", (req, res) => {
	if ( req.headers.username == "wantyapps" && req.headers.password == "pass123" ) {
		res.send('{"username": "wantyapps", "password": "oao"}');
	} else {
		res.send("Incorrect username or password.");
	};
});

const PORT = 5000;

app.listen(PORT, () => console.log(`Server is listening on port ${PORT}`));
