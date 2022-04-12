import axios from "axios";
// import { FormContent } from "@/interfaces/FormContent";

export default {
    async uploadImg(arg: string) {
        const formData = new FormData();
        formData.append("userfile", arg);
        const data = await axios.post('path/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        return data;
    }
};