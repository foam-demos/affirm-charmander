import * as foam from '@foam-ai/browser-opentelemetry';
import { FOAM_API_KEY, IS_PRODUCTION_ENV } from './config';

foam.init({
  serviceName: 'merchant-integration-sdk',
  isProduction: IS_PRODUCTION_ENV,
  apiKey: FOAM_API_KEY,
  captureErrors: true,
  capturePerformance: true,
  sampleRate: 1.0,
});