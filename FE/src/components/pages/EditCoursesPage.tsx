import React from "react";
import Page from "../common/Page";
import CoursesContainer from "../elements/CoursesContainer";
import { Divider, Typography } from "@mui/material";

const EditCoursesPage: React.FC = () => {
  return (
    <Page>
      <Typography variant={"h3"}>Courses</Typography>
      <Divider sx={{ marginBottom: "20px", marginTop: "20px" }} />
      <CoursesContainer />
    </Page>
  );
};

export default EditCoursesPage;
