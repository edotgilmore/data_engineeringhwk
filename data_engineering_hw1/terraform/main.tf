
 # Connect to gcp using ADC (identity verification)
 provider "google" {
   project = var.project
   region  = var.region
   zone    = var.zone
 }

 /* add these data blocks */
 
 # This data source gets a temporary token for the service account
 data "google_service_account_access_token" "default" {
   provider               = google
   target_service_account = "<terraform-runner@project-88b4df8e-a00d-4d64-bea.iam.gserviceaccount.com>"
   scopes                 = ["https://www.googleapis.com/auth/cloud-platform"]
   lifetime               = "3600s"
 }
 
 # This second provider block uses that temporary token and does the real work
 provider "google" {
   alias        = "impersonated"
   access_token = data.google_service_account_access_token.default.access_token
   project      = var.project
   region       = var.region
   zone         = var.zone
 }
# Create a GCS bucket with lifecycle rules
 resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-bucket-88b4df8e-a00d-4d64-bea"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}