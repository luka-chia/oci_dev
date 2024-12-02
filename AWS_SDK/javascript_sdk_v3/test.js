import { CognitoIdentityClient } from "@aws-sdk/client-cognito-identity";
import { fromCognitoIdentityPool } from "@aws-sdk/credential-provider-cognito-identity";

// Set up the identity pool credentials provider
const region = "us-east-1"; // Replace with your region
const identityPoolId = "us-east-1:01d3fc37-9bd0-4e05-958a-115dfed78a01"; // Your Cognito Identity Pool ID

const credentials = fromCognitoIdentityPool({
    client: new CognitoIdentityClient({ region }),
    identityPoolId, // Your identity pool ID
});

// Now, the AWS SDK will use these credentials for API requests
