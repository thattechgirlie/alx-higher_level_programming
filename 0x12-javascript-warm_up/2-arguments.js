#!/usr/bin/node
if (process.argc.length === 2){
	console.log('No Argument');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
