import { deleteRequest, getRequest, postRequest, putRequest } from "./base";
import Course from "../types/course";

export const createCourse = (
  data: Omit<Course, "tests" | "lections" | "id">
) => {
  return postRequest("course", data);
};

export const getCoursesFullInfo = () => {
  return getRequest("course");
};

export const deleteCourse = (id: number) => {
  return deleteRequest(`course/${id}`);
};

export const updateCourse = (
  id: number,
  data: Omit<Course, "tests" | "lections" | "id">
) => {
  return putRequest(`course/${id}`, data);
};
