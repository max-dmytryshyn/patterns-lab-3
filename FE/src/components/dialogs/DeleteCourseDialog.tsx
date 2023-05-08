import React from "react";
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  IconButton,
  Typography,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";

interface DeleteCourseDialogProps {
  isOpen: boolean;
  courseTitle: string;
  onDelete: () => void;
  onClose: () => void;
}

const DeleteCourseDialog: React.FC<DeleteCourseDialogProps> = ({
  isOpen,
  courseTitle,
  onClose,
  onDelete,
}) => {
  return (
    <Dialog open={isOpen} onClose={onClose}>
      <DialogTitle
        sx={{
          display: "flex",
          justifyContent: "right",
          alignItems: "center",
        }}
      >
        <IconButton
          onClick={onClose}
          sx={{ marginLeft: "10px", marginRight: "-15px" }}
        >
          <CloseIcon />
        </IconButton>
      </DialogTitle>
      <DialogContent sx={{ padding: "40px", width: "400px" }}>
        <Typography
          variant={"h6"}
        >{`Do you want to delete course "${courseTitle}"?`}</Typography>
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
          No
        </Button>
        <Button
          onClick={onDelete}
          variant={"outlined"}
          color={"error"}
          sx={{ width: "200px" }}
        >
          Yes
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default DeleteCourseDialog;
