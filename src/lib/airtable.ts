/**
 * Airtable helper functions
 *
 * This module provides a simple wrapper around the Airtable REST API. It
 * reads configuration from environment variables (`AIRTABLE_API_KEY`,
 * `AIRTABLE_BASE_ID`, and optional table names) and exposes functions for
 * fetching data. When integrating with other tables (e.g. Leads, Metrics),
 * follow the pattern used in `fetchContacts`.
 */

export interface ContactRecord {
  id: string;
  Name?: string;
  Email?: string;
  Persona?: string;
  Stage?: string;
  [key: string]: any;
}

/** Fetch all records from the contacts table. */
export async function fetchContacts(): Promise<ContactRecord[]> {
  const apiKey = process.env.AIRTABLE_API_KEY;
  const baseId = process.env.AIRTABLE_BASE_ID;
  const tableName = process.env.AIRTABLE_CONTACTS_TABLE || 'Contacts';
  if (!apiKey || !baseId) {
    console.warn('Airtable credentials are missing');
    return [];
  }
  const url = `https://api.airtable.com/v0/${baseId}/${encodeURIComponent(
    tableName
  )}`;
  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  });
  if (!response.ok) {
    console.error('Failed to fetch contacts from Airtable:', response.status);
    return [];
  }
  const data = (await response.json()) as {
    records: { id: string; fields: Record<string, any> }[];
  };
  return data.records.map((record) => ({ id: record.id, ...record.fields }));
}