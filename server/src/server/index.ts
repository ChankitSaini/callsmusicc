import Express from "express";

import env from "../env";
import routers from "./routers";

const app = Express();

app.use(routers);

export default () => app.listen(env.PORT);
