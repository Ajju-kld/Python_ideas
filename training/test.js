const nodemailer = require('nodemailer');

async function sendPDF() {
  // Create a transporter
  const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
      user: "daniassecrets@gmail.com",
      pass: 'sUtpoj-fezwir-2vognu',
    },
  });

  // Define the email options
  const mailOptions = {
    from: 'daniassecrets@gmail.com',
    to: 'stralaxia@gmail.com',
    subject: 'Sending PDF',
    text: 'Please find the attached PDF file.',
    attachments: [
      {
        filename: 'example.pdf',
        path: './example.pdf',
      },
    ],
  };

  try {
    // Send the email
    const info = await transporter.sendMail(mailOptions);
    console.log('Email sent:', info.response);
  } catch (error) {
    console.error('Error sending email:', error);
  }
}

 sendPDF();
