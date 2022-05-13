const mongoose = require("mongoose");

const StudentSchema = mongoose.Schema(
  {
    name: String,
    rollno: Number,
    wad_marks: Number,
    cc_marks: Number,
    dsbda_marks: Number,
    cns_marks: Number,
    ai_marks: Number,
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("Student", StudentSchema);
