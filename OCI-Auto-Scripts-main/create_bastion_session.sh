#!/bin/bash

# OCI Bastion Session Creator and SSH Tunnel Starter
#
# This script automates the creation of an Oracle Cloud Infrastructure (OCI) bastion session
# for port forwarding and then establishes the SSH tunnel to connect to private resources.
#
# Usage: ./create_bastion_session.sh [bastion_id] [target_port] [target_private_ip] [local_port]
#
# Arguments:
#   bastion_id: OCID of the bastion (default: predefined)
#   target_port: Port on the target instance (default: 22)
#   target_private_ip: Private IP of the target instance (default: 10.0.1.90)
#   local_port: Local port for forwarding (default: 2222)
#
# Requirements:
# - OCI CLI installed and configured with proper authentication
# - jq installed for JSON parsing
# - SSH private and public keys in ~/.ssh/ (id_rsa and id_rsa.pub)
# - OCI_CLI_PASS_PHRASE environment variable set if your OCI API key is encrypted
#
# The script performs the following steps:
# 1. Creates a port-forwarding bastion session using OCI CLI
# 2. Extracts the session OCID from the response
# 3. Constructs and displays the SSH command for port forwarding
# 4. Executes the SSH command to establish the tunnel
#
# Example:
#   export OCI_CLI_PASS_PHRASE=your_passphrase
#   ./create_bastion_session.sh
#
# This will create a session and start forwarding local port 2222 to 10.0.1.90:22 via the bastion.

# Default values from bastion file
DEFAULT_BASTION_ID="ocid1.bastion.oc1.ap-seoul-1.amaaaaaaak7gbriak2xz3eb2jphlckydf6tkdvmhghgp2qsnd5yvdnc2cu"
DEFAULT_TARGET_PORT=22
DEFAULT_TARGET_PRIVATE_IP="10.0.1.90"
DEFAULT_LOCAL_PORT=2222
DEFAULT_SSH_PRIVATE_KEY="/Users/stevli/.ssh/id_rsa"
DEFAULT_SSH_PUBLIC_KEY_FILE="/Users/stevli/.ssh/id_rsa.pub"
DEFAULT_REGION="ap-seoul-1"
DEFAULT_SESSION_TTL=10800
DEFAULT_KEY_TYPE="PUB"

# Parse command line arguments
BASTION_ID="${1:-$DEFAULT_BASTION_ID}"
TARGET_PORT="${2:-$DEFAULT_TARGET_PORT}"
TARGET_PRIVATE_IP="${3:-$DEFAULT_TARGET_PRIVATE_IP}"
LOCAL_PORT="${4:-$DEFAULT_LOCAL_PORT}"

# Use defaults for other parameters
SSH_PRIVATE_KEY="$DEFAULT_SSH_PRIVATE_KEY"
SSH_PUBLIC_KEY_FILE="$DEFAULT_SSH_PUBLIC_KEY_FILE"
REGION="$DEFAULT_REGION"
SESSION_TTL="$DEFAULT_SESSION_TTL"
KEY_TYPE="$DEFAULT_KEY_TYPE"
DISPLAY_NAME="ssh${TARGET_PORT}"

# Check if oci CLI is available
if ! command -v oci &> /dev/null; then
    echo "Error: OCI CLI is not installed or not in PATH" >&2
    exit 1
fi

# Check if jq is available
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed or not in PATH" >&2
    exit 1
fi

# Create the bastion session
echo "Creating bastion session..." >&2
SESSION_OUTPUT=$(oci bastion session create-port-forwarding \
    --bastion-id "$BASTION_ID" \
    --target-port "$TARGET_PORT" \
    --target-private-ip "$TARGET_PRIVATE_IP" \
    --ssh-public-key-file "$SSH_PUBLIC_KEY_FILE" \
    --key-type "$KEY_TYPE" \
    --session-ttl "$SESSION_TTL" \
    --display-name "$DISPLAY_NAME" \
    --wait-for-state "SUCCEEDED" \
    --region "$REGION" \
    --output json 2>&1)

# Check if command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Failed to create bastion session" >&2
    echo "$SESSION_OUTPUT" >&2
    exit 1
fi

# Extract session OCID from JSON output, skipping any non-JSON text
SESSION_OCID=$(echo "$SESSION_OUTPUT" | sed -n '/{/,$p' | jq -r '.data.resources[0].identifier' 2>/dev/null || echo "$SESSION_OUTPUT" | grep "ocid1.bastionsession" | head -1 | awk '{print $1}')

if [ -z "$SESSION_OCID" ] || [ "$SESSION_OCID" = "null" ]; then
    echo "Error: Failed to extract session OCID from response" >&2
    echo "$SESSION_OUTPUT" >&2
    exit 1
fi
# Construct and output the SSH command
SSH_COMMAND="ssh -i $SSH_PRIVATE_KEY -N -L $LOCAL_PORT:$TARGET_PRIVATE_IP:$TARGET_PORT -p 22 $SESSION_OCID@host.bastion.$REGION.oci.oraclecloud.com"

# Execute the SSH command to start the port forwarding tunnel
echo "Starting SSH port forwarding tunnel on one terminal with below command" >&2
echo "$SSH_COMMAND"

echo "and then in another terminal tab, you could start to access your target instance via locahost $LOCAL_PORT with your target instance private key">&2
echo "sample as : ssh -i <your_VM_privatekey> -p $LOCAL_PORT ubuntu@127.0.0.1"
