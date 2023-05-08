import React, { useEffect, useState } from "react";
import CourseItem from "./CourseItem";
import Course from "../../types/course";
import { createCourse, getCoursesFullInfo } from "../../api/course";
import { Box, Button } from "@mui/material";
import EditCourseDialog from "../dialogs/EditCourseDialog";

const CoursesContainer: React.FC = () => {
  const [courses, setCourses] = useState<Course[]>([]);
  const [addCourseDialogState, setAddCourseDialogState] =
    useState<boolean>(false);

  const removeCourse = (id: number) => {
    setCourses(
      courses.reduce<Course[]>((accum, course) => {
        if (course.id === id) {
          return accum;
        }
        return [...accum, course];
      }, [])
    );
  };

  const editCourse = (
    id: number,
    data: Omit<Course, "tests" | "lections" | "id">
  ) => {
    setCourses(
      courses.reduce<Course[]>((accum, course) => {
        if (course.id === id) {
          const newCourse = {
            ...course,
            title: data.title,
            description: data.description,
          };
          return [...accum, newCourse];
        }
        return [...accum, course];
      }, [])
    );
  };

  const addCourse = (newCourse: Course) => {
    setCourses([newCourse, ...courses]);
  };

  useEffect(() => {
    getCoursesFullInfo().then((data) => {
      setCourses(data);
    });
  }, []);
  return (
    <>
      <EditCourseDialog
        isOpen={addCourseDialogState}
        onClose={() => setAddCourseDialogState(false)}
        onSubmit={(data) => {
          createCourse(data).then((response) => {
            addCourse(response);
            setAddCourseDialogState(false);
          });
        }}
      />
      <Box
        sx={{
          display: "flex",
          flexWrap: "wrap",
          overflowY: "auto",
          height: "900px",
        }}
      >
        <Button
          sx={{
            width: "500px",
            height: "300px",
            margin: "10px",
            fontSize: "100px",
          }}
          color={"success"}
          variant={"outlined"}
          onClick={() => setAddCourseDialogState(true)}
        >
          +
        </Button>
        {courses.map((course) => (
          <CourseItem
            course={course}
            removeCourse={removeCourse}
            ediCourse={editCourse}
            key={course.id}
          />
        ))}
      </Box>
    </>
  );
};

export default CoursesContainer;
