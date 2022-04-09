import axios from "axios";
import { FormData } from "@/interfaces/FormData";

export default {
    async uploadImg(arg: FormData) {
        try {
            const data = await axios.post('path/', arg, {
                headers: {}
            });
            return data;
        } catch (err) {
            throw err;
        }
    }
};