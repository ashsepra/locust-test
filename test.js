var request = require('request');

request({
  method: 'POST',
  url: 'https://private-anon-d04ae31239-apiary.apiary-mock.com/authorization',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic dGVzdEB0ZXN0LnRlc3Q6dGVzdHRlc3Q='
  },
  body: "tokenDescription=What%27s%20this%20token%20for%3F&tokenRegenerate=false"
}, function (error, response, body) {
  console.log('Status:', response.statusCode);
  console.log('Headers:', JSON.stringify(response.headers));
  console.log('Response:', body);
});