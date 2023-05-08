import Test from "./test";
import Lection from "./lection";

interface Course {
  id: number;
  title: string;
  description: string;
  tests: Test[];
  lections: Lection[];
}

export default Course;
