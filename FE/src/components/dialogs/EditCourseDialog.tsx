import React, { useState } from "react";
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  IconButton,
  TextField,
} from "@mui/material";
import { makeStyles } from "@mui/styles";
import CloseIcon from "@mui/icons-material/Close";
import Course from "../../types/course";

const useStyles = makeStyles({
  formLabel: {
    fontSize: "20px",
    textAlign: "center",
    width: "100%",
    marginTop: "16px",
    marginBottom: 0,
  },
  formContainer: {
    marginTop: "16px",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  submitButton: {
    marginTop: "16px",
  },
});

interface EditCourseDialogProps {
  course?: Omit<Course, "tests" | "lections">;
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (data: Omit<Course, "tests" | "lections" | "id">) => void;
}

const EditCourseDialog: React.FC<EditCourseDialogProps> = ({
  course,
  isOpen,
  onSubmit,
  onClose,
}) => {
  const classes = useStyles();
  const [data, setData] = useState<Omit<Course, "tests" | "lections" | "id">>(
    course
      ? course
      : {
          title: "",
          description: "",
        }
  );

  const handleFieldChange = (
    event: React.ChangeEvent<HTMLTextAreaElement | HTMLInputElement>
  ) => {
    const { name, value } = event.target;
    setData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return (
    <Dialog open={isOpen} onClose={onClose}>
      <DialogTitle
        sx={{
          display: "flex",
          justifyContent: "right",
          alignItems: "center",
        }}
      >
        <p className={classes.formLabel}>{course ? "Edit" : "Add"} Course</p>
        <IconButton onClick={onClose} sx={{ position: "absolute" }}>
          <CloseIcon />
        </IconButton>
      </DialogTitle>
      <DialogContent sx={{ padding: "40px", width: "400px", height: "325px" }}>
        <div className={classes.formContainer}>
          <TextField
            sx={{ marginBottom: "16px", width: "400px" }}
            label="Title"
            name="title"
            value={data.title}
            onChange={(event) => handleFieldChange(event)}
          />
          <TextField
            sx={{ marginBottom: "16px", width: "400px" }}
            fullWidth
            label="Description"
            name="description"
            multiline
            rows={8}
            value={data.description}
            onChange={(event) => handleFieldChange(event)}
          />
        </div>
      </DialogContent>
      <DialogActions
        sx={{
          display: "flex",
          justifyContent: "space-around",
          paddingBottom: "30px",
        }}
      >
        <Button
          onClick={onClose}
          variant={"outlined"}
          color={"primary"}
          sx={{ width: "200px" }}
        >
          Cancel
        </Button>
        <Button
          onClick={() => {
            onSubmit(data);
            setData({
              title: "",
              description: "",
            });
          }}
          variant={"outlined"}
          color={"error"}
          sx={{ width: "200px" }}
          disabled={!data.title || !data.description}
        >
          Submit
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default EditCourseDialog;
