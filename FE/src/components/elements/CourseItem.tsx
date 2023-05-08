import React, { useState } from "react";
import {
  Card,
  CardContent,
  CardHeader,
  IconButton,
  Typography,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/DeleteOutline";
import EditIcon from "@mui/icons-material/EditOutlined";
import Course from "../../types/course";
import DeleteCourseDialog from "../dialogs/DeleteCourseDialog";
import { deleteCourse, updateCourse } from "../../api/course";
import EditCourseDialog from "../dialogs/EditCourseDialog";

interface CourseItemProps {
  course: Course;
  removeCourse: (id: number) => void;
  ediCourse: (
    id: number,
    data: Omit<Course, "tests" | "lections" | "id">
  ) => void;
}

const CourseItem: React.FC<CourseItemProps> = ({
  course,
  removeCourse,
  ediCourse,
}) => {
  const [deleteDialogState, setDeleteDialogState] = useState<boolean>(false);
  const [editDialogState, setEditDialogState] = useState<boolean>(false);

  return (
    <>
      <DeleteCourseDialog
        isOpen={deleteDialogState}
        courseTitle={course.title}
        onDelete={() => {
          deleteCourse(course.id).then(() => {
            removeCourse(course.id);
            setDeleteDialogState(false);
          });
        }}
        onClose={() => setDeleteDialogState(false)}
      />
      <EditCourseDialog
        course={course}
        isOpen={editDialogState}
        onClose={() => setEditDialogState(false)}
        onSubmit={(data) => {
          updateCourse(course.id, data).then(() => {
            ediCourse(course.id, data);
            setEditDialogState(false);
          });
        }}
      />
      <Card sx={{ width: "500px", height: "300px", margin: "10px" }}>
        <CardHeader
          sx={{ textAlign: "left", paddingBottom: "0" }}
          action={
            <>
              <IconButton
                aria-label="settings"
                color={"primary"}
                onClick={() => setEditDialogState(true)}
              >
                <EditIcon />
              </IconButton>
              <IconButton
                onClick={() => setDeleteDialogState(true)}
                aria-label="settings"
                color={"error"}
              >
                <DeleteIcon />
              </IconButton>
            </>
          }
          title={course.title}
        />
        <CardContent>
          <Typography textAlign={"left"}>
            <b>Lections:</b>{" "}
            {course.tests.length !== 0 &&
              course.lections
                .reduce<string>(
                  (accum, lection) => accum + lection.title + ", ",
                  ""
                )
                .slice(0, -2) + "."}
          </Typography>
          <Typography textAlign={"left"}>
            <b>Tests:</b>{" "}
            {course.tests.length !== 0 &&
              course.tests
                .reduce<string>((accum, test) => accum + test.title + ", ", "")
                .slice(0, -2) + "."}
          </Typography>
          <Typography textAlign={"left"}>
            <b>Description:</b> {course.description}
          </Typography>
        </CardContent>
      </Card>
    </>
  );
};

export default CourseItem;
