#!/usr/bin/node
const number = Number(process.argv[2]);
if (!number) console.log('Missing size');
for (let i = 0; i < number; i++) {
  let line = '';
  for (let j = 0; j < number; j++) { line += 'X'; }
  console.log(line);
}
