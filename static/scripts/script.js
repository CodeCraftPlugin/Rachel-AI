let mediaRecorder;
let chunks = [];
let timerInterval;
let elapsedTime = 0;

// Format time to display as HH:MM:SS
function formatTime(seconds) {
  const hrs = Math.floor(seconds / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;
  return `${hrs.toString().padStart(2, "0")}:${mins
    .toString()
    .padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
}

// Start recording and timer
function startRecording() {
  navigator.mediaDevices
    .getUserMedia({ audio: true })
    .then(function (stream) {
      // Start the timer
      elapsedTime = 0;
      if (!timerInterval) {
        timerInterval = setInterval(() => {
          elapsedTime++;
          document.getElementById("output").innerText = formatTime(elapsedTime);
        }, 1000);
      }

      // Start the recording
      mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.start();

      mediaRecorder.addEventListener("dataavailable", function (event) {
        chunks.push(event.data);
      });
    })
    .catch(function (error) {
      console.error("Error accessing microphone:", error);
    });
}

// Stop recording and timer
function stopRecording() {
  if (mediaRecorder) {
    mediaRecorder.stop();

    // Stop the timer
    clearInterval(timerInterval);
    timerInterval = null; // Reset timer interval
  }

  mediaRecorder.addEventListener("stop", function () {
    const audioBlob = new Blob(chunks, { type: "audio/webm" });

    // Prepare form data to send the audio file
    const formData = new FormData();
    formData.append("audio", audioBlob, "recording.webm"); // 'recording.webm' is the file name

    // Send the audio file to the server
    fetch("/audio", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          console.log("Audio file successfully uploaded!");
        } else {
          console.error("Failed to upload the audio file.");
        }
      })
      .catch((error) => {
        console.error("Error while uploading the audio file:", error);
      });

    // Clear the chunks array for the next recording session
    chunks = [];
  });
}
