#!/usr/bin/node
if (isNaN(process.argv[2])) 
{
	console.log("Missing number of occurrences");
} 
else
{
	let num = parseInt(process.argv[2]);
	let i = 0;
	for (i = 0; i < num; i++)
	{
		console.log("C is fun");
	}
}
