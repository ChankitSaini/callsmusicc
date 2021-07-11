import client from "./client";
import server from "./server";

(async () => {
  await client();
  server();
})();
