import { ENDPOINTS } from "../constants/apiConstants";
import { BaseService } from "./BaseService";

const getToken = (username, password) => {
  return BaseService.post(`${ENDPOINTS.ACCOUNT}/token`, {
    username: username,
    password: password,
  });
};

export const { AccountService } = { getToken };
