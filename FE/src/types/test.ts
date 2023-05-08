import Question from "./question";

export enum TestType {
  PRACTISE = "PRACTISE",
  EXAM = "EXAM",
}

interface Test {
  id: number;
  title: string;
  type: TestType;
  description: string;
  questions: Question[];
}

export default Test;
