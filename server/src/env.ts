import { config } from "dotenv";
import { cleanEnv, str, num } from "envalid";

config();

export default cleanEnv(process.env, {
    PORT: num({ default: 8080 }),
    STRING_SESSION: str(),
    API_ID: num(),
    API_HASH: str(),
});
