#!/usr/bin/node
const fs = require('fs');
fs.writeFile(prcess.argv[2], process.argv[3], error =>{
	if (error){
		console.log(error);
	}
});
