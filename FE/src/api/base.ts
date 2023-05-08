import axios from "axios";
import { BE_URL } from "../config";

export const getRequest: (uri: string, params?: any) => Promise<any> = async (
  uri,
  params
) => {
  const response = await axios.get(`${BE_URL}/${uri}`, { params: params });
  return response.data;
};

export const postRequest: (
  uri: string,
  data: any,
  params?: any
) => Promise<any> = async (uri, data, params) => {
  const response = await axios.post(`${BE_URL}/${uri}`, data, {
    params: params,
  });
  return response.data;
};

export const putRequest: (
  uri: string,
  data: any,
  params?: any
) => Promise<any> = async (uri, data, params) => {
  const response = await axios.put(`${BE_URL}/${uri}`, data, {
    params: params,
  });
  return response.data;
};

export const deleteRequest: (
  uri: string,
  params?: any
) => Promise<any> = async (uri, params) => {
  const response = await axios.delete(`${BE_URL}/${uri}`, {
    params: params,
  });
  return response.data;
};
