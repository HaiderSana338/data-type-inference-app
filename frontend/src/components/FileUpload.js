//FileUpload.js
import React, { useState } from 'react';
import axios from 'axios';
import { Container, Row, Col, Form, Button, Alert, Spinner, Card } from 'react-bootstrap';
import { FaUpload } from 'react-icons/fa';
import './FileUpload.css';  // Import custom CSS

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://localhost:8000/data/upload/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResponse(res.data);
    } catch (err) {
      setError('Error uploading the file. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className="upload-container">
      <Row className="justify-content-center">
        <Col md={8}>
          <Card className="shadow p-4">
            <h2 className="text-center mb-4">
              <FaUpload /> Upload CSV or Excel File
            </h2>

            <Form onSubmit={handleUpload}>
              <Form.Group controlId="formFile" className="mb-3">
                <Form.Control type="file" onChange={handleFileChange} accept=".csv, .xlsx" />
              </Form.Group>
              <div className="d-grid">
                <Button type="submit" variant="primary" disabled={!file || loading}>
                  {loading ? <Spinner animation="border" size="sm" /> : 'Upload'}
                </Button>
              </div>
            </Form>

            {error && <Alert variant="danger" className="mt-4">{error}</Alert>}
            {response && (
              <Card className="mt-4">
                <Card.Body>
                  <h4>Inferred Data Types</h4>
                  <pre>{JSON.stringify(response, null, 2)}</pre>
                </Card.Body>
              </Card>
            )}
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default FileUpload;