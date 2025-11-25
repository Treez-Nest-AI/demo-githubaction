const {hello} = require("../handler");

test("returns 200 status code", async () => {
    const response = await hello();
    expect(response.statusCode).toBe(200);
});

test("returns correct message", async () => {
    const response = await hello();
    const body = JSON.parse(response.body);
    expect(body.message).toBe("Hello From nodejs demo service");
});